
def KelvinToFahrenheit(Temperature):
    try:
        
        assert (Temperature >= 0),"Colder than absolute zero!"
        return ((Temperature-273)*1.8)+32


    except AssertionError as e:
        print(e)

    except IndentationError as e:
        print(e)

    except SyntaxError as e:
        print(e)

print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
print(KelvinToFahrenheit(-5))

