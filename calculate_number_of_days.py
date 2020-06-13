import datetime
import calendar
import math


# payment of debt
balance = 5000
interest_rate = 0.13
mothly_payment = 500

today = datetime.date.today()
days_in_current_month = calendar.monthrange(today.year, today.month)[1]
days_till_end_of_month = days_in_current_month - today.day

start_date = today + datetime.timedelta(days=days_till_end_of_month + 1)
end_date = start_date

payment_date = start_date
while balance > 0:
    interest_charge = (interest_rate / 12) * balance
    balance += interest_charge
    balance -= mothly_payment
    balance = 0 if balance < 0 else round(balance, 2)
    days_till_end_of_month = calendar.monthrange(payment_date.year, payment_date.month)[1]
    payment_date = payment_date + datetime.timedelta(days=days_till_end_of_month)
    # print(payment_date, balance)

end_date = payment_date
print('The last payment is on: {}'.format(end_date))

# weight loss
current_weight = 81.6
goal_weight = 75
weekly_loss = 0.3

start_date = datetime.date.today()
weight_date = start_date
while current_weight > goal_weight:
    current_weight -= weekly_loss
    current_weight = round(current_weight, 3)
    weight_date += datetime.timedelta(weeks=1)
    # print(weight_date, current_weight)

print('You reach your weight goal: {} which is {} weeks'.format(weight_date, (weight_date - start_date).days // 7))

# subscribers

current_subs = 100
goal_subs = 500
average_subs_in_day = 10

start_date = datetime.date.today()
nof_days = math.ceil((goal_subs - current_subs) / average_subs_in_day)

end_date = start_date + datetime.timedelta(days=nof_days)
print(f'You have reached your subs goal in {nof_days} days which is {end_date}')

# python learning 1000 hours

hours_a_day = 0.5
python_learning_goal = 500

start_date = datetime.date.today() - datetime.timedelta(days=36)
days_to_goal = math.ceil(python_learning_goal / hours_a_day)

goal_achive_date = start_date + datetime.timedelta(days=days_to_goal)
print(f'You will have {python_learning_goal} hours of python learned by {goal_achive_date}')

