from flet import Container, GridView, Page, Text, alignment, border, border_radius, colors, ElevatedButton, app
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def main(page: Page):
    page.title = "AlertDialog examples"

    def launchWeb(e):
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get('https://www.google.com/')

    page.add(
        Container(
            ElevatedButton("Open dialog", on_click=launchWeb),
            alignment=alignment.Alignment(0, 0),
            # bgcolor=colors.AMBER_100,
            # border=border.all(1, colors.AMBER_400),
            # border_radius=border_radius.all(5),
        )
    )


app(target=main)
