import matplotlib.pyplot as plt
plt.tight_layout()

# 512 bytes
plt.plot([2, 4, 8, 16, 32, 64, 100], [305, 917, 2140, 4226, 4924, 4489, 4414], 'go-', label='Throughput (512 bytes)', linewidth=2, color='#34c3b9')

# 1024 bytes
plt.plot([2, 4, 8, 16, 32, 64, 100], [305, 917, 2140, 3550, 3099, 3579, 3450], 'go-', label='Throughput (1024 bytes)', linewidth=2, color='#e99579')

# 1500 bytes

plt.plot([2, 4, 8, 16, 32, 64, 100], [305, 917, 2139, 1894, 1899, 2327, 1920], 'go-', label='Throughput (1500 bytes)', linewidth=2, color='#0066ff')

plt.ylabel('Vazão (Kbps)', fontsize='large',)
plt.xlabel('Número de nós da rede (Unidade)', fontsize='large')
plt.title("Vazão na rede Halteres \n com tamanho de pacotes 512 bytes, 1024 bytes e 1500 bytes", fontsize=20	, fontweight='bold')
plt.legend()
plt.show()
