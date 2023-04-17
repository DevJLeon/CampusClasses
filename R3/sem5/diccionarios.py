empleado = {"nombre":"Sergio Medina", "cargo":"programador", "salario":40000000}

empleado["nombre"]
empleado.get("nombre")
empleado["email"]="algo@correo.com"
print(empleado.get("email","NO ENCONTRADO"))