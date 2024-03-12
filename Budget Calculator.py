import json
import os
import matplotlib.pyplot as plt

class BudgetTracker:
    def _init_(self, filename="transactions.json"):
        self.filename = filename
        self.transactions = []
        self.load_transactions()

    def load_transactions(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.transactions = json.load(file)

    def save_transactions(self):
        with open(self.filename, 'w') as file:
            json.dump(self.transactions, file, indent=4)

    def add_transaction(self, category, amount, transaction_type):
        transaction = {"category": category, "amount": amount, "type": transaction_type}
        self.transactions.append(transaction)
        self.save_transactions()

    def calculate_budget(self):
        income = sum(transaction["amount"] for transaction in self.transactions if transaction["type"] == "income")
        expenses = sum(transaction["amount"] for transaction in self.transactions if transaction["type"] == "expense")
        remaining_budget = income - expenses
        return remaining_budget

    def analyze_expenses(self):
        expense_categories = {}
        for transaction in self.transactions:
            if transaction["type"] == "expense":
                category = transaction["category"]
                amount = transaction["amount"]
                if category in expense_categories:
                    expense_categories[category] += amount
                else:
                    expense_categories[category] = amount
        return expense_categories

def main():
    budget_tracker = BudgetTracker()

    while True:
        print("\nBUDGET TRACKER")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Remaining Budget")
        print("4. Analyze Expenses")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter income category: ")
            amount = float(input("Enter income amount: "))
            budget_tracker.add_transaction(category, amount, "income")
            print("Income added.")

        elif choice == "2":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            budget_tracker.add_transaction(category, amount, "expense")
            print("Expense added.")

        elif choice == "3":
            remaining_budget = budget_tracker.calculate_budget()
            print(f"Remaining budget: {remaining_budget}")

        elif choice == "4":
            expense_categories = budget_tracker.analyze_expenses()
            print("\nEXPENSE ANALYSIS:")
            for category, amount in expense_categories.items():
                print(f"{category}: {amount}")
            
            # Plotting the bar graph
            plt.bar(expense_categories.keys(), expense_categories.values(), color='skyblue')
            plt.xlabel('Expense Categories')
            plt.ylabel('Amount')
            plt.title('Expense Analysis')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
