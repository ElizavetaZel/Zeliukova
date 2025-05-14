import matplotlib.pyplot as plt
import numpy as np
with open('settings1.txt', 'r') as settings_file:
    settings = settings_file.readlines()
    discretisation = float(settings[0].split(':')[1].strip().split()[0])  
    quantize_step = float(settings[1].split(':')[1].strip().split()[0])  
with open('data1.txt', 'r') as data_file:
    adc_data = [float(line.strip()) for line in data_file.readlines()]
    adc_data[0] = 0
voltage = np.array(adc_data) * quantize_step
time = np.arange(len(voltage)) / discretisation
plt.figure(figsize=(10, 6))
plt.plot(time, voltage, color='blue', linestyle='-', linewidth=1, label='V(t)')
plt.scatter(time[::10], voltage[::10], color='red', s=10, label='Измерения (каждое 10-е)')  
plt.xlabel('Время, с', fontsize=12)
plt.ylabel('Напряжение, В', fontsize=12)
plt.title('График зависимости напряжения от времени\nЗарядка и разрядка конденсатора',
          fontsize=14, loc='center', wrap=True)
plt.grid(True, which='major', linestyle='--', color='gray', alpha=0.7)
plt.grid(True, which='minor', linestyle=':', color='lightblue', alpha=0.5)
plt.minorticks_on()
plt.xlim(0, max(time))
plt.ylim(0, max(voltage) * 1.1)
plt.legend(fontsize=10)
charging_time = time[np.argmax(voltage)]
discharging_time = time[-1] - charging_time
plt.text(0.95 * max(time), 0.9 * max(voltage), 
         f'Время зарядки: {charging_time:.2f} с\nВремя разрядки: {discharging_time:.2f} с',
         bbox=dict(facecolor='white', alpha=0.8), ha='right')
plt.savefig('voltage_plot.svg', format='svg')
plt.show()