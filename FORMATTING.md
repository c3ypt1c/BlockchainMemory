# Formatting

I have a simple Python formatting scheme that so far has 2 rules:

## From higher indentation to lower indenation
The number of empty lines after indentation should be more than current indentation level minus wanted indentation level.

## Immediately after indentation
Lines that have immediately have been indented almost never have a space after their indentee.

##Example :)
```python
#Chickens is an array of chick(s)
#Chick is a set of feet, body, feathers and wings

for Chick in Chickens:
    SmileAt( Chick )
    feet, body, feathers, wings = Chick
    pet( body )
    for foot in feet:
        check( foot )
        
    for feather in feathers:
        love( feather )
            
    for wing in wings: #Notice only 1 line above
        poke( wing )   #Notice poke is immediately after indentatee (the 'for' statement)
            
            
SmileAtAll( Chickens ) #:) Notice the 2 lines above.
CleanCoop()
```
