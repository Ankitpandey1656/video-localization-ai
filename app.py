import streamlit as st
import subprocess, os, glob

st.set_page_config(page_title="YouTube AI Assistant", layout="wide")

st.title("YouTube AI Assistant")

col1, col2 = st.columns([2, 1])

with col1:
    url = st.text_input("YouTube URL:")
    mode = st.radio("Processing Mode:", ["Transcript Only", "Transcript + Hindi Audio"])

    if st.button("Start Processing"):
        if url:
            # Convert the selected UI option into the backend processing mode.
            mode_arg = "Full" if mode == "Transcript + Hindi Audio" else "Basic"

            with st.status("Processing video...", expanded=True) as status:
                st.write("Starting backend processing...")

                # Execute the backend processor with the provided URL and mode.
                result = subprocess.run(
                    ["python", "processor.py", url, mode_arg],
                    capture_output=True,
                    text=True
                )

                if result.returncode == 0:
                    status.update(label="Processing completed", state="complete")
                    st.success("Video processed successfully.")
                else:
                    status.update(label="Processing failed", state="error")
                    st.error(result.stderr)

            # Refresh the interface to display newly generated files.
            st.rerun()
        else:
            st.error("Please enter a valid YouTube URL.")

with st.sidebar:
    st.header("History & File Management")

    # Collect all generated transcript and audio files.
    files = glob.glob("job_*.txt") + glob.glob("job_*.mp3")

    # Extract unique job IDs from generated filenames.
    jobs = set([f.split("_")[1] for f in files])

    for job_id in sorted(list(jobs), reverse=True):
        with st.expander(f"Job: {job_id}"):

            # Retrieve all files associated with the current job.
            job_files = glob.glob(f"job_{job_id}_*")

            for f in job_files:
                col_a, col_b = st.columns([3, 1])

                col_a.write(os.path.basename(f))

                # Download the selected file.
                with open(f, "rb") as file_data:
                    col_b.download_button(
                        "Download",
                        file_data,
                        file_name=os.path.basename(f),
                        key=f"dl_{f}"
                    )

                # Delete the selected file.
                if col_b.button("Delete", key=f"del_{f}"):
                    os.remove(f)
                    st.rerun()