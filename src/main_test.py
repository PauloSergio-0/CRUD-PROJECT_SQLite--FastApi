# data = dict(Nome="Paulo", idade= 12, altura=1.90)
# data ={'sexo': "m"}

# print("keys")
# print(tuple(data.keys()))

# print("\nValues")
# print(tuple(data.values()))

def Filter_table(data: dict):
        sql_filter = """SELECT * FROM Carro """
        condicoes = []


        if ("marca" in data) and  (data["marca"] is not None):
        
            condicoes.append("Marca_veiculo = ?")
        
            
        if ("Modelo" in data) and  (data["Modelo"] is not None):
            condicoes.append("Modelo_carro = ?")
            
        if ("qtde" in data) and (data["qtde"] is not None):
            condicoes.append("Modelo_carro = ?")
            
        if condicoes:
            sql_filter += " WHERE "+" AND ".join(condicoes)

            
            
        print(sql_filter)
        
d = {"marca":"ford", "modelo": "gt"}

Filter_table(d)
        
        