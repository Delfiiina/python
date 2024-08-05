#Ejercicio 1
#a)

otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

diferencia_porcentaje_DaltoMin = ((otros_cursos_min * 100) / dalto_curso) - 100
print (f"El más rápido tarda un {int(diferencia_porcentaje_DaltoMin)} % más que el de Dalto")
diferencia_porcentaje_DaltoMax = (( otros_cursos_max * 100) / dalto_curso) - 100
print (f"El más lento tarda un {int(diferencia_porcentaje_DaltoMax)} % más que el de Dalto")
diferencia_porcentaje_DaltoPromedio = (( otros_cursos_promedio * 100) / dalto_curso) - 100
print (f"El promedio tarda un {int(diferencia_porcentaje_DaltoPromedio)} % más que el de Dalto")

diferencia_porcentaje_DaltoMin = 100 - ((dalto_curso * 100) / otros_cursos_min) 
print (f"El curso de Dalto tarda un {int(diferencia_porcentaje_DaltoMin)} % menos que el mínimo")
diferencia_porcentaje_DaltoMax = 100 - ((dalto_curso * 100) / otros_cursos_max) 
print (f"El curso de Dalto tarda un {int(diferencia_porcentaje_DaltoMax)} % menos que el máximo")
diferencia_porcentaje_DaltoPromedio = 100 - ((dalto_curso * 100) / otros_cursos_promedio)
print (f"El curso de Dalto tarda un {int(diferencia_porcentaje_DaltoPromedio)} % menos que el promedio")

#b