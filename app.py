from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    print("Hosting...")
    return(
        """
            <!DOCTYPE html>
            <html lang="en">
                <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>DevOps - Projeto Web (Exemplificação)</title>
                <style>
                    .root {
                        margin: auto;
                        width: 60%;
                        background-color: rgb(206, 206, 206);
                        border-radius: 5px;
                        padding: 3rem;
                        margin-top: 20vh;
                    }
                    .hidden {
                        display: none;
                    }
                    .granted {
                        display: block;
                        color: green;
                    }
                    .denied {
                        display: block;
                        color: red;
                    }
                </style>
                </head>
                <body>
                <div class="root">
                    <h1>DevOps - Projeto Web (Exemplificação)</h1>
                    <h3> Página de Cadastramento</h3>
                    <form>
                        <input type="text" name="user" id="user" placeholder="usuário">
                        <input type="password" name="password" id="password" placeholder="senha">
                        <button id="submit">Submeter</button>
                    </form>
                    <p id="access" class="hidden">Escondido</p>
                </div>

                <script>
                    document.getElementById("submit").addEventListener("click", function(event) {
                        event.preventDefault();
                        let user = document.getElementById("user").value;
                        let password = document.getElementById("password").value;
                        console.log(`User: ${user}, Password: ${password}`);

                        if(user === "root" && password === "root") {
                            console.log("POW!");
                            if (document.getElementById("access").classList.contains("hidden")) {
                                document.getElementById("access").classList.remove("hidden");
                            }
                            document.getElementById("access").classList.add("granted");
                            document.getElementById("access").innerText = "Acesso permitido!"
                        } else {
                            if (document.getElementById("access").classList.contains("hidden")) {
                                document.getElementById("access").classList.remove("hidden");
                            }
                            document.getElementById("access").classList.add("denied");
                            document.getElementById("access").innerText = "Acesso negado!"
                        }
                    })
                </script>
                </body>
            </html>
        """
    )

if __name__ == "__main__":
    print("Hosting...")
    app.run(host="0.0.0.0", port=8081, debug=True)