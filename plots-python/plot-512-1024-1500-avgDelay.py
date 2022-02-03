import matplotlib.pyplot as plt
plt.tight_layout()

# 512 bytes
plt.plot([2, 4, 8, 16, 32, 64, 100], [0.00753832, 0.0092156, 0.0151843, 0.0254031, 0.0198125, 0.00980476, 0.00699673], 'go-', label='Average Delay (512 bytes)', linewidth=3, color='#34c3b9')

# 1024 bytes
plt.plot([2, 4, 8, 16, 32, 64, 100], [0.00978745, 0.0141358, 0.0270466, 0.445353, 0.302961, 0.174801, 0.106967], 'go-', label='Average Delay (1024 bytes)', linewidth=3, color='#e99579')

# 1500 bytes
plt.plot([2, 4, 8, 16, 32, 64, 100], [0.0119103, 0.0195283, 0.03863, 0.294404, 0.179316, 0.103227, 0.0542161], 'go-', label='Average Delay (1500 bytes)', linewidth=3, color='#0066ff')

plt.ylabel('Atraso médio (Segundos)', fontsize='large',)
plt.xlabel('Número de nós da rede (Unidade)', fontsize='large')
plt.title("Atraso médio na rede Halteres \n com tamanho de pacotes 512 bytes, 1024 bytes e 1500 bytes", fontsize=20, fontweight='bold')
plt.legend()
plt.show()
