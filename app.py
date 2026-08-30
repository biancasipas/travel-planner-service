from flask import Flask
from flask_restx import Api, Resource, fields

from services.planejamento import (
    calcular_gasto_por_dia,
    classificar_orcamento,
    calcular_dias
)


app = Flask(__name__)

api = Api(
    app,
    version="1.0",
    title="Travel Planner Service",
    description="API secundária responsável pelo planejamento de viagens."
)


# Modelo para o POST /planejamento
planejamento_model = api.model("Planejamento", {
    "destino": fields.String(required=True),
    "dias": fields.Integer(required=True),
    "orcamento": fields.Float(required=True)
})


# Modelo para o POST /calcular-dias
datas_viagem_model = api.model("DatasViagem", {
    "data_inicio": fields.String(required=True),
    "data_fim": fields.String(required=True)
})


# Rota inicial
@api.route("/")
class Home(Resource):

    def get(self):
        return {
            "mensagem": "Travel Planner Service funcionando!"
        }, 200


# Calcula o gasto médio por dia
@api.route("/planejamento")
class Planejamento(Resource):

    @api.expect(planejamento_model)
    def post(self):
        dados = api.payload

        dias = dados["dias"]
        orcamento = dados["orcamento"]

        gasto_por_dia = calcular_gasto_por_dia(
            orcamento,
            dias
        )

        return {
            "destino": dados["destino"],
            "dias": dias,
            "orcamento": orcamento,
            "gasto_por_dia": gasto_por_dia
        }, 200


# Classifica o orçamento
@api.route("/classificar-orcamento/<orcamento>")
class ClassificarOrcamento(Resource):

    def get(self, orcamento):

        orcamento = float(orcamento)

        classificacao = classificar_orcamento(
            orcamento
        )

        return {
            "orcamento": orcamento,
            "classificacao": classificacao
        }, 200


# Calcula a quantidade de dias da viagem
@api.route("/calcular-dias")
class CalcularDias(Resource):

    @api.expect(datas_viagem_model)
    def post(self):
        dados = api.payload

        quantidade_dias = calcular_dias(
            dados["data_inicio"],
            dados["data_fim"]
        )

        return {
            "data_inicio": dados["data_inicio"],
            "data_fim": dados["data_fim"],
            "quantidade_dias": quantidade_dias
        }, 200


if __name__ == "__main__":
    app.run(debug=True, port=5001)