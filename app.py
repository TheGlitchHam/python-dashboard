import dash
import dash_html_components as html

# Init app

app = dash.Dash(__name__)

# App defintion

app.layout = html.Div()

#Runner

if __name__ == "__main__":
    app.run_server(debug=True)