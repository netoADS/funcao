def cm(notas):
    total = sum(notas)
    media = total/len(notas)
    return media
    
notas = [7.5, 8.0, 6.5, 9.0]
media = cm(notas)
print('a média é:', media)