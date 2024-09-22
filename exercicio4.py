#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#• SP – R$67.836,43
#• RJ – R$36.678,66
#• MG – R$29.229,88
#• ES – R$27.165,48
#• Outros – R$19.849,53
sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53
faturamento_total = sp + rj + mg + es + outros
percentual_sp = (sp / faturamento_total) * 100
percentual_rj = (rj / faturamento_total) * 100
percentual_mg = (mg / faturamento_total) * 100
percentual_es = (es / faturamento_total) * 100
percentual_outros = (outros / faturamento_total) * 100
print("Percentual de representação por estado:")
print(f"SP: {percentual_sp:.2f}%")
print(f"RJ: {percentual_rj:.2f}%")
print(f"MG: {percentual_mg:.2f}%")
print(f"ES: {percentual_es:.2f}%")
print(f"Outros: {percentual_outros:.2f}%")