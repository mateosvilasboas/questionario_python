fat_sp = 67836.43
fat_rj = 36678.66
fat_mg = 29229.88
fat_es = 27165.48
fat_outros = 19849.53

soma_fat = fat_sp + fat_rj + fat_mg + fat_es + fat_outros

print("percentual de faturamento sp: {fat_sp}%". format(
    fat_sp = round((fat_sp/soma_fat)*100, 2)))
print("percentual de faturamento rj: {fat_rj}%". format(
    fat_rj = round((fat_rj/soma_fat)*100, 2)))
print("percentual de faturamento rj: {fat_mg}%". format(
    fat_mg = round((fat_mg/soma_fat)*100, 2)))
print("percentual de faturamento rj: {fat_es}%". format(
    fat_es = round((fat_es/soma_fat)*100, 2)))
print("percentual de faturamento rj: {fat_outros}%". format(
    fat_outros = round((fat_outros/soma_fat)*100, 2)))
