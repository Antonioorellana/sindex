def main() -> None:
    import customtkinter as ctk

    app = ctk.CTk()
    app.geometry("400x300")

    frame = ctk.CTkFrame(app)
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    label = ctk.CTkLabel(frame, text="Hello World")
    label.pack(pady=50)

    app.mainloop()


if __name__ == "__main__":
    main()
