import matplotlib.pyplot as plt
from Expense import Expense
import Expense
import collections

expenses = Expense.Expenses()
expenses.read_expenses("data/spending_data.csv")

spending_categories = []

for expenses in expenses.list:
    spending_categories.append(expenses.category)

spending_counter = collections.Counter(spending_categories)
# print(spending_counter)

top5 = spending_counter.most_common(5)
# print(top5)

categories, count = zip(*top5)
# print(categories)
# print(count)

fig, ax = plt.subplots()
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')
plt.show()