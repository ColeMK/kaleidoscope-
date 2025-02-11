from process_video import stylize_video
import sqlite3
import os
from pathlib import Path
def main():
    kaliedoscope_dir = os.path.split(os.getcwd())[0]
    upload_path = os.path.join(kaliedoscope_dir, 'web', 'kaleidoscope', 'uploads')
    dowload_folder = os.path.join(kaliedoscope_dir, 'web', 'kaleidoscope', 'downloads')
    model_path = "style_ukiyoe_pretrained"
    database = "../web/kaleidoscope/db.sqlite3"

    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM mainpage_mymodel')

    count = int(cur.fetchone()[0])
    totalfiles = count # makes them the same to start

    specific_id = totalfiles
    cur.execute('SELECT * FROM mainpage_mymodel WHERE id = ?', (specific_id,))
    print(cur.fetchone()[1])
    while True:
        cur.execute('SELECT COUNT(*) FROM mainpage_mymodel')
        totalfiles = int(cur.fetchone()[0])
        if count<totalfiles:
            count += 1
            specific_id = totalfiles
            cur.execute('SELECT * FROM mainpage_mymodel WHERE id = ?', (specific_id,))
            #TODO: Cole what does this do? If we using an operating system with \ dir system this will not work.
            process_file = str(((cur.fetchone()[1]).split('/',1)[1])[:-4].replace(" ", "_")) #should split by first instance of /
            #process stuff 
            uploaded_video_path = os.path.join(upload_path, process_file) + ".mp4"
            stylized_video_path = f"{os.path.join(dowload_folder, process_file)}_{model_path}.mp4"
            print("stylize video activate")
            stylize_video(uploaded_video_path, stylized_video_path, model_path)


    print(count)


    cur.close()
    conn.close()

if __name__ == '__main__':
    main()