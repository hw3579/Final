import matplotlib.pyplot as plt

# 创建一个包含精度数据的字典
accuracy = {
    'normal': 98.4,
    'horizontal_line': 95.6,
    'vertical_line': 80.0,
    'slope': 96.1,
    'other': 95.2
}

# 创建直方图
plt.bar(accuracy.keys(), accuracy.values())
plt.xlabel('Category')
plt.ylabel('Accuracy (%)')
plt.title('Model Accuracy on Test Set')
plt.savefig('./fig/assistplot/accuracy.eps')
plt.show()


import matplotlib.pyplot as plt

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

# 创建直方图
plt.bar(accuracy.keys(), accuracy.values())
plt.xlabel('Angle')
plt.ylabel('Accuracy (%)')
plt.title('Normal Accuracy on Different Angles')
plt.savefig('./fig/assistplot/angle_accuracy.eps')
plt.show()