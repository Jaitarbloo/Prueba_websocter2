import reflex as rx

config = rx.Config(
    app_name="Prueba_websocker2",
    show_built_with_reflex=True,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)