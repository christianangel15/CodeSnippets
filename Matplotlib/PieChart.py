# PieChart Only good option if there are less than 5 or 6 labels

from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

Slices = [35917, 36443, 47544, 55466, 59219]

labels = ['Java', 'Python', 'SQL', 'HTML/CSS', 'JavaScript']

expl = [0, 0.1, 0, 0, 0]
plt.pie(Slices, labels=labels, shadow = True, explode=expl,
        wedgeprops={'edgecolor':'black'}, autopct = '%1.1f%%', startangle=180)

plt.title('Most Popular Languages, 2019')
plt.tight_layout()
plt.show()
