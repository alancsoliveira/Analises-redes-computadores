import matplotlib.pyplot as plt
plt.tight_layout()

# 512 bytes
plt.plot([2, 4, 8, 16, 32, 64, 100], [100, 100, 99, 95, 68, 37, 25], 'go-', label='Packets Success Ratio (512 bytes)', linewidth=3, color='#34c3b9')

# 1024 bytes
plt.plot([2, 4, 8, 16, 32, 64, 100], [100, 100, 99, 85, 47, 31, 20], 'go-', label='Packets Success Ratio (1024 bytes)', linewidth=3, color='#e99579')

# 1500 bytes
plt.plot([2, 4, 8, 16, 32, 64, 100], [100, 100, 99, 54, 31, 21, 11], 'go-', label='Packets Success Ratio (1500 bytes)', linewidth=3, color='#0066ff')

plt.ylabel('Taxa de sucesso de pacotes (%)', fontsize='large',)
plt.xlabel('Número de nós da rede (Unidade)', fontsize='large')
plt.title("Taxa de sucesso de pacotes na rede Halteres \n com tamanho de pacotes 512 bytes, 1024 bytes e 1500 bytes", fontsize=20, fontweight='bold')
plt.legend()
plt.show()
