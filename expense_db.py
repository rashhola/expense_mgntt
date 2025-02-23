import uuid #importing the library for universal unique identifier that uses machines physical IDs etc
from datetime import datetime, timezone

#creating an expense object with title and amount
class Expense:
    def __init__(self, title: str, amount: float):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = float(amount)
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at

    def update(self, title: str = None, amount: float = None):# Updating the method to modify an existing expense
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = float(amount)
        self.updated_at = datetime.now(timezone.utc)

    def to_dict(self):# creating a disctionary to store the class.
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

class ExpenseDB:# managing multiple expense using the ExpenseDb (the database)
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)

    def remove_expense(self, expense_id: str):
        self.expenses = [expense for expense in self.expenses if expense.id != expense_id]

    def get_expense_by_id(self, expense_id: str):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expense_by_title(self, title: str):
        return [expense for expense in self.expenses if expense.title.lower() == title.lower()]

    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]
    


