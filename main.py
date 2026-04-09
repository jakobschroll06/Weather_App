import customtkinter as ctk

from API_Calls import getAlerts, getForcast

class Display(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.label = None
        self.scrollingFrame = None

        self.title("Weather App")
        self.geometry("640x480")

        self.mainColor = "#7d812c"
        self.accentColor = "#dfdfde"
        self.textColor = "#224e4e"
        self.textFont = "Courier"

        self.configure(fg_color=self.mainColor)

        self.MakeMenu()


    def MakeMenu(self):
        # Title Label
        self.label = ctk.CTkLabel(self, text="WEATHER", font=(self.textFont, 28, "bold"), text_color=self.textColor)
        self.label.pack(pady=20)

        # Scrolling Frame
        self.scrollingFrame = ctk.CTkScrollableFrame(self, fg_color=self.accentColor, corner_radius=0)
        self.scrollingFrame.pack(padx=20, pady=20, fill="both", expand=True)
        self.AddForcast()

    def AddForcast(self):
        #Clear (Not used at the moment)
        for i in self.scrollingFrame.winfo_children():
            i.destroy()

        # Change at somepoint to input any lat and lon
        forcast = getForcast(50,78)

        if forcast:
            for i in range(len(forcast)):

                lbl = ctk.CTkLabel(
                    self.scrollingFrame,
                    text=f"• {forcast[i]['name']}: {forcast[i]['detailedForecast']}",
                    text_color=self.textColor,
                    font=(self.textFont, 14, "bold"),
                    wraplength=500,
                    justify="left"
                )

                lbl.pack(anchor="w", padx=20, pady=5)

if __name__ == '__main__':
    app = Display()
    app.mainloop()

    # state = str(input("Input State (e.g. WA): "))
    # state = "KY"
    # print(getAlerts(state))
    #
    # print("#" * 200)
    #
    # print(getForcast(50, 78))

