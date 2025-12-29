import reflex as rx

config = rx.Config(
    app_name="Prueba_websocker2",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)