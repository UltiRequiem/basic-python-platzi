def run():
    poblacion_paises = {
	'Argentina': 44_938_712,
	'Brasil': 210_147_125,
	'Colombia': 50_372_424
    }
#    print(poblacion_paises['Brasil'])
    for pais,poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')  

if __name__ == '__main__':
    run()
