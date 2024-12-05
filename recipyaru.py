import folium
import pandas as pd
from folium.plugins import HeatMap







mapa = folium.Map(location=[-28.9350,-49.4847], zoom_start=15)

HeatMap([[-28.9350,-49.4847]], radius=20).add_to(mapa)

folium.Marker(
    location=[-28.9497921977204, -49.506302204579136],
    tooltip="Pontos de lixos reciclaveis!",
    popup="Ponto de lixo reciclavel.",
    icon=folium.Icon(icon="glyphicon glyphicon-trash", color="green"),
).add_to(mapa)

folium.Marker(
    location=[-28.946955660611753, -49.45945225349725],
    tooltip="Pontos de lixos reciclaveis!",
    popup="Ponto de lixo reciclavel.",
    icon=folium.Icon(icon="glyphicon glyphicon-trash", color="green"),
).add_to(mapa)

folium.Marker(
    location=[-28.946284240281805, -49.51182301762548],
    tooltip="Pontos de lixos reciclaveis!",
    popup="Ponto de lixo reciclavel.",
    icon=folium.Icon(icon="glyphicon glyphicon-trash", color="green"),
).add_to(mapa)

folium.Marker(
    location=[-28.97323863039396, -49.484169821280496],
    tooltip="Pontos de lixos reciclaveis!",
    popup="Ponto de lixo reciclavel.",
    icon=folium.Icon(icon="glyphicon glyphicon-trash", color="green"),
).add_to(mapa)

folium.Marker(
    location=[-29.003831535967237, -49.551749436603146],
    tooltip="Pontos de lixos reciclaveis!",
    popup="Ponto de lixo reciclavel.",
    icon=folium.Icon(icon="glyphicon glyphicon-trash", color="green"),
).add_to(mapa)

folium.Marker(
    location=[-29.003311893266076, -49.552421279971355],
    tooltip="Pontos de lixos reciclaveis!",
    popup="Ponto de lixo reciclavel.",
    icon=folium.Icon(icon="glyphicon glyphicon-trash", color="green"),
).add_to(mapa)

folium.Marker(
    location=[-28.946955660611753, -49.45945225349725],
    tooltip="Pontos de lixos reciclaveis!",
    popup="Ponto de lixo reciclavel.",
    icon=folium.Icon(icon="glyphicon glyphicon-trash", color="green"),
).add_to(mapa)

folium.Marker(
    location=[-28.940070163958413, -49.46826940594797],
    tooltip="Pontos de Perigo",
    popup="Ponto de Lixo na rua",
    icon=folium.Icon(icon="glyphicon glyphicon-flag", color="red"),
).add_to(mapa)

folium.Marker(
    location=[-28.943954723528627, -49.47199416735317],
    tooltip="Pontos de Perigo!",
    popup="Ponto Acumulando lixo.",
    icon=folium.Icon(icon="glyphicon glyphicon-flag", color="red"),
).add_to(mapa)

folium.Marker(
    location=[-28.950629549330365, -49.46660141605255],
    tooltip="Pontos de Perigo!",
    popup="Ponto Acumulando lixo.",
    icon=folium.Icon(icon="glyphicon glyphicon-flag", color="red"),
).add_to(mapa)

radius1 = 50
folium.CircleMarker(
    location=[-28.93533914631541, -49.489604125109025],
    radius=radius1,
    color="red",
    weight=3,
    fill=True,
    fill_color="red",
    fill_opacity=0.6,
    opacity=1,
    popup="Area em Perigo",
).add_to(mapa)

folium.Circle(
    location=[-28.93613221660972, -49.488598162971186],
    radius=radius1,
    color="red",
    weight=1,
    fill_opacity=0.6,
    opacity=1,
    fill_color="red",
    fill=True,  
    popup="Area em perigo",
    tooltip="Perigo",
).add_to(mapa)

radius2 = 70
radius3 = 30

folium.Circle(
    location=[-28.94331542292824, -49.473273575686044],
    radius=radius2,
    color="red",
    weight=1,
    fill_opacity=0.6,
    opacity=1,
    fill_color="red",
    fill=True,  
    popup="Area em perigo",
    tooltip="Perigo",
).add_to(mapa)


folium.Circle(
    location=[-28.940084070340966, -49.46990461961127],
    radius=radius3,
    color="red",
    weight=1,
    fill_opacity=0.6,
    opacity=1,
    fill_color="red",
    fill=True,  
    popup="Area em perigo",
    tooltip="Perigo",
).add_to(mapa)




folium.Circle(
    location=[-28.941335798360285, -49.46955074985951],
    radius=radius2,
    color="red",
    weight=1,
    fill_opacity=0.6,
    opacity=1,
    fill_color="red",
    fill=True,  
    popup="Area em perigo",
    tooltip="Perigo",
).add_to(mapa)


folium.Circle(
    location=[-28.946917546863062, -49.49294369570994],
    radius=radius2,
    color="red",
    weight=1,
    fill_opacity=0.6,
    opacity=1,
    fill_color="red",
    fill=True,  
    popup="Area em perigo",
    tooltip="Perigo",
).add_to(mapa)

folium.Marker(
    location=[-28.938421938848407, -49.4637233406409],
    tooltip="Ponto Adequeado",
    popup="Ponto Adequado",
    icon=folium.Icon(icon="glyphicon glyphicon-star", color="orange"),
).add_to(mapa)

folium.Marker(
    location=[-28.945079157420246, -49.496556115487884],
    tooltip="Ponto Adequeado",
    popup="Ponto Adequado",
    icon=folium.Icon(icon="glyphicon glyphicon-star", color="orange"),
).add_to(mapa)

folium.Marker(
    location=[-28.935802148199418, -49.46936835275988],
    tooltip="Ponto Adequeado",
    popup="Ponto Adequado",
    icon=folium.Icon(icon="glyphicon glyphicon-star", color="orange"),
).add_to(mapa)

folium.Marker(
    location=[-28.94447507683942, -49.48539936856836],
    tooltip="Ponto Adequeado",
    popup="Ponto Adequado",
    icon=folium.Icon(icon="glyphicon glyphicon-star", color="orange"),
).add_to(mapa)

folium.Marker(
    location=[-28.936635897803907, -49.4797241043072],
    tooltip="Ponto Adequeado",
    popup="Ponto Adequado",
    icon=folium.Icon(icon="glyphicon glyphicon-star", color="orange"),
).add_to(mapa)


folium.Marker(
    location=[-28.936598340205617, -49.479842121496766],
    tooltip="Ponto Adequeado",
    popup="Ponto Adequado",
    icon=folium.Icon(icon="glyphicon glyphicon-star", color="orange"),
).add_to(mapa)

folium.Marker(
    location=[-28.93431407886402, -49.48647909591434],
    tooltip="Ponto Adequeado",
    popup="Ponto Adequado",
    icon=folium.Icon(icon="glyphicon glyphicon-star", color="orange"),
).add_to(mapa)



folium.Marker(
    location=[-28.936973915589085, -49.48167675247328],
    tooltip="Ponto Adequeado",
    popup="Ponto Adequado",
    icon=folium.Icon(icon="glyphicon glyphicon-star", color="orange"),
).add_to(mapa)


folium.Circle(
    location=[-28.946174030913188, -49.47170459563454],
    radius=radius2,
    color="red",
    weight=1,
    fill_opacity=0.6,
    opacity=1,
    fill_color="red",
    fill=True,  
    popup="Area em perigo",
    tooltip="Perigo",
).add_to(mapa)


df = pd.DataFrame(
    data=[["Plasticos", "Metais"], ["Garrafa Pet", "Bateria de notebook"]], columns=["Descartavel", "Nao Descartavel"]
)


html = df.to_html(
    classes="table table-striped table-hover table-condensed table-responsive"
)

popup = folium.Popup(html)

folium.Marker([-28.938860550594566, -49.48117095050957], popup=popup).add_to(mapa)

df2 = pd.DataFrame(
    data=[["Plasticos", "Metais"], ["Garrafa Pet = 9\n \n Pontas de cigarro = 23", "Cabos e fios[sucatas] = 6"]], columns=["Descartavel", "Nao Descartavel"]
)


html = df2.to_html(
    classes="table table-striped table-hover table-condensed table-responsive"
)

popup = folium.Popup(html)

folium.Marker([-28.928150819456295, -49.48695891144138], popup=popup).add_to(mapa)



#-28.94501730217142, -49.48508071999875

folium.Marker(
    location=[-28.945023717154786, -49.48499763878299],
    tooltip="Casa do Pyaru!",
    popup="Mantenha a cidade limpa humano!",
    icon=folium.Icon(icon="glyphicon glyphicon-home", color="green"),
).add_to(mapa)




mapa.save("mapa.html")