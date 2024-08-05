import tkinter as tk
from get_details import get_car_details

def update_ui(details):
    license_number_value.config(text=details.get("mispar_rechev", "לא נמצא"))
    tozeret_nm_value.config(text=details.get("tozeret_nm", "לא נמצא"))
    ramat_gimur_value.config(text=details.get("ramat_gimur", "לא נמצא"))
    shnat_yitzur_value.config(text=details.get("shnat_yitzur", "לא נמצא"))
    kinuy_mishari_value.config(text=details.get("kinuy_mishari", "לא נמצא"))
    tzeva_rechev_value.config(text=details.get("tzeva_rechev", "לא נמצא"))
    tokef_dt_value.config(text=details.get("tokef_dt", "לא נמצא"))
    michvan_aharon_value.config(text=details.get("mivchan_acharon_dt", "לא נמצא"))
    baalut_value.config(text=details.get("baalut", "לא נמצא"))
    sug_delek_value.config(text=details.get("sug_delek_nm", "לא נמצא"))
    tzamig_ahori_value.config(text=details.get("zmig_ahori", "לא נמצא"))
    tzamig_kidmi_value.config(text=details.get("zmig_kidmi", "לא נמצא"))

def check_input():
    value = entry.get()
    if value:
        result = get_car_details(value)
        if result:
            update_ui(result[0])
        else:
            update_ui({"mispar_rechev": "לא נמצא"})

root = tk.Tk()
root.geometry("600x800")
root.title("בדוק רכב")

# Title
title_label = tk.Label(root, text="בדוק רכב!", font=("Arial", 28))
title_label.pack(pady=20)

# License number input
input_frame = tk.Frame(root)
input_frame.pack(pady=20)

license_label = tk.Label(input_frame, text="הכנס מספר רישוי: ", font=("Arial", 18))
license_label.pack(side="left")

entry = tk.Entry(input_frame, font=("Arial", 16), width=20, bg="gray")
entry.pack(side="left", padx=10)

check_button = tk.Button(input_frame, text="בדוק", font=("Arial", 14), command=check_input)
check_button.pack(side="left", padx=10)

# Results Display
result_frame = tk.Frame(root, pady=20, padx=20)
result_frame.pack()


def create_result_row(frame, label_text):
    row_frame = tk.Frame(frame)
    row_frame.pack(fill="x", pady=5)

    label = tk.Label(row_frame, text=label_text, font=("Arial", 14))
    label.pack(side="right")

    value = tk.Label(row_frame, text="לא נמצא", font=("Arial", 14))
    value.pack(side="right", padx=10)

    return value

license_number_value = create_result_row(result_frame, " :לוחית רישוי")
tozeret_nm_value = create_result_row(result_frame, " :חברה")
ramat_gimur_value = create_result_row(result_frame, " :רמת גימור")
shnat_yitzur_value = create_result_row(result_frame, " :שנת יצור")
kinuy_mishari_value = create_result_row(result_frame, " :דגם מנוע")
tzeva_rechev_value = create_result_row(result_frame, " :צבע")
tokef_dt_value = create_result_row(result_frame, " :תוקף רישיון רכב")
michvan_aharon_value = create_result_row(result_frame, " :מבחן טסט אחרון")
baalut_value = create_result_row(result_frame, " :בעלות נוכחית")
sug_delek_value = create_result_row(result_frame, " :סוג דלק")
tzamig_ahori_value = create_result_row(result_frame, " :מידת צמיג אחורי")
tzamig_kidmi_value = create_result_row(result_frame, " :מידת צמיג קדמי")

root.mainloop()
