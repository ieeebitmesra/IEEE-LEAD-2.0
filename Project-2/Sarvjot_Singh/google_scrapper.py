import tkinter as tk
import webbrowser
from google_data import google_fun


def callback(url):
    webbrowser.open_new(url)


def print_jobs(query):

    # GOOGLE

    google_obj = google_fun(query)

    for i in range(-1, min(5, len(google_obj["names"]))):

        if(i == -1):

            frm_results.rowconfigure(i+1, weight=1, minsize=50)

            frm_result_cell = tk.Frame(master=frm_results)
            frm_result_cell.grid(row=i+1, column=0, padx=5, pady=5)

            data_btn = tk.Button(
                master=frm_result_cell,
                text="Results from Google",
                foreground="black",
                background="white",
                cursor="hand2",
                command=lambda e="https://google.com": callback(e),
                width=25,
                height=4
            )
            data_btn.pack()

        else:

            # data

            str = google_obj["names"][i]
            url = google_obj["links"][i]

            # layout

            frm_results.rowconfigure(i+1, weight=1, minsize=50)

            frm_result_cell = tk.Frame(master=frm_results)
            frm_result_cell.grid(row=i+1, column=0, padx=5, pady=5)

            data_btn = tk.Button(
                master=frm_result_cell,
                text=str,
                foreground="purple",
                background="yellow",
                cursor="hand2",
                command=lambda e=url: callback(e),
                width=25,
                height=6
            )
            data_btn.pack()


def init_print_jobs():
    query = query_entry.get()
    print_jobs(query)


window = tk.Tk()

#  Frames

# Three frames that add up to our primary vertical grid

for i in range(0, 3):
    window.rowconfigure(i, weight=1, minsize=50)

window.columnconfigure(0, weight=1, minsize=75)

frm_query = tk.Frame(master=window)
frm_query.grid(row=0, column=0, padx=5, pady=5)

frm_button = tk.Frame(master=window)
frm_button.grid(row=1, column=0, padx=5, pady=5)

frm_results = tk.Frame(master=window)
frm_results.grid(row=2, column=0, padx=5, pady=5)

#  Result Frames

for i in range(0, 5):
    frm_results.rowconfigure(i, weight=1, minsize=50)

frm_results.columnconfigure(0, weight=1, minsize=75)


# Labels and Entries

query_label = tk.Label(master=frm_query, text="Enter Query")
query_entry = tk.Entry(master=frm_query, fg="black", bg="white", width=50)

query_label.pack(side=tk.LEFT)
query_entry.pack(side=tk.LEFT)

go_btn = tk.Button(
    master=frm_button,
    text="Go!!",
    foreground="white",
    background="black",
    width="3",
    height="1",
    command=init_print_jobs
)

go_btn.pack()

window.mainloop()
