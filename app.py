from flask import Flask
from flask_restx import Api, Resource, fields


app = Flask(__name__)

api = Api(
    app,
    version="1.0",
    title="Travel Planner Service",
    description="API secundária responsável pelo planejamento de viagens."
)


planejamento_model = api.model("Planejamento", {
    "destino": fields.String(required=True),
    "dias": fields.Integer(required=True),
    "orcamento": fields.Float(required=True)
})


@api.route("/")
class Home(Resource):

    def get(self):
        return {
            "mensagem": "Travel Planner Service funcionando!"
        }, 200


@api.route("/planejamento")
class Planejamento(Resource):

    @api.expect(planejamento_model)
    def post(self):
        dados = api.payload

        dias = dados["dias"]
        orcamento = dados["orcamento"]

        gasto_por_dia = orcamento / dias

        return {
            "destino": dados["destino"],
            "dias": dias,
            "orcamento": orcamento,
            "gasto_por_dia": round(gasto_por_dia, 2)
        }, 200

@api.route("/classificar-orcamento/<orcamento>")
class ClassificarOrcamento(Resource):

    def get(self, orcamento):

        orcamento = float(orcamento)

        if orcamento < 3000:
            classificacao = "Econômico"
        elif orcamento < 10000:
            classificacao = "Moderado"
        else:
            classificacao = "Confortável"

        return {
            "orcamento": orcamento,
            "classificacao": classificacao
        }, 200


if __name__ == "__main__":
    app.run(debug=True, port=5001)