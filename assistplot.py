import matplotlib.pyplot as plt

# 创建一个包含精度数据的字典
accuracy = {
    'normal': 98.4,
    'horizontal line': 95.6,
    'vertical line': 80.0,
    'slope': 96.1,
    'other': 95.2
}

# 创建直方图
plt.plot(list(accuracy.keys()), list(accuracy.values()), marker='o')
plt.xlabel('Category', fontsize=15)
plt.tick_params(labelsize=12)
plt.ylabel('Accuracy (%)', fontsize=15)
plt.ylim(0, 100)
plt.title('Model Accuracy on Test Set')
plt.savefig('./fig/assistplot/accuracy.eps')
plt.show()

# 创建一个包含精度数据的字典
accuracy = {
    '8': 80,
    '8.5': 81.5,
    '9': 83.5,
    '9.5': 93.3,
    '10': 96.6,
    '10.5': 88.8,
    '11': 84.2,
    '11.5': 66.6,
    '12': 62.2
}

# Create a line plot with markers at data points
plt.plot(list(accuracy.keys()), list(accuracy.values()), marker='o')
plt.xlabel('Angle', fontsize=15)
plt.tick_params(labelsize=15)
plt.ylabel('Accuracy (%)', fontsize=15)
plt.ylim(0, 100)
plt.title('Normal Accuracy on Different Angles')
plt.savefig('./fig/assistplot/angle_accuracy.eps')
plt.show()

# 创建一个包含精度数据的字典
accuracy = {
    'bad': 94.1,
    'good': 98.2,
    'normal': 94.7,
    'other': 95.0
}

# 创建直方图
# Change the bar plot to a line plot with markers at data points
plt.plot(list(accuracy.keys()), list(accuracy.values()), marker='o')
plt.xlabel('Category', fontsize=15)
plt.tick_params(labelsize=15)
plt.ylabel('Accuracy (%)', fontsize=15)
plt.ylim(0, 100)
plt.title('Normal Accuracy on Different Angles')
plt.savefig('./fig/assistplot/angle_accuracy2.eps')
plt.show()