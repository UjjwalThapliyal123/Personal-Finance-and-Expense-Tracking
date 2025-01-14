SELECT * FROM project_track_expense.combined_expenses;
use project_track_expense;

select * from combined_expenses;

-- 1. Query to find the total values
select count(*) from combined_expenses;

-- 2.Find the records for month of august
select * 
from  combined_expenses
where date  between '2024-08-1' and '2024-08-31';

-- 3. Find the total amount of month August and date
select sum(amount) as total_amount_of_month,extract(month from date) as month
from combined_expenses
where date  between '2024-08-1' and '2024-08-31'
group by month
order by total_amount_of_month desc
limit 1;

 -- 4 Total amounts of different months
select sum(amount) as total_amount_of_month,extract(month from date) as month
From combined_expenses
where date  between '2024-01-1' and '2024-12-31'
group by month
order by total_amount_of_month desc;


-- 5 Total amounts of all the months
select sum(amount) as total_amount_of_month
from combined_expenses
where date  between '2024-01-1' and '2024-12-31'
order by total_amount_of_month 
limit 1;

-- 6. Month with the max amount
select extract(month from date) as month, sum(amount) as the_total_amount
from combined_expenses
where date between '2024-01-01' AND '2024-12-31'
GROUP BY month
ORDER BY the_total_amount DESC
limit 1;

-- 7.Get average of amount and cashback
select avg(amount) as Average_amount ,avg(cashback) as Average_cashback
from combined_expenses;

-- 8 Get date and amount when category is Rent and payment_mode is gpay
select date , Amount,categories,payment_mode
from combined_expenses
where categories ='Rent' and payment_mode='Gpay';

-- 9 update the description values 
SET SQL_SAFE_UPDATES = 0;

update combined_expenses
set description='I enjoys watching movies at the theatre'
where categories="Entertainment";

-- 10 Changing/updating more values 
update combined_expenses
set description=case
	when categories='taxes' then 'I keeps track of my receipts and expenses'
    when categories='Groceries' then 'High Quality incredients'
    when categories='Travel' then 'Exploring new destination and adventures'
    when categories='Utilities' then 'Bills are dued every month'
    when categories='Subscription' then 'Subcribed to interesting services'
    when categories='Investment' then 'Diversifying the money in stock, real-estate and FD increases finacial stabilty for the future'
    when categories='Insurance' then 'Investment in any like of vehicle make people free'
    when categories='Rent' then 'The rent of the apartment is due at 1 of every month'
    else description
end;


-- 10. Get cashback more than average cashback received
select cashback,date,payment_mode
from combined_expenses
where cashback>(select avg(cashback) from combined_expenses);



-- 11.  Get amount more than average cashback received
select amount,date,payment_mode
from combined_expenses
where amount>(select avg(amount) from combined_expenses);

-- 12. get amount between 3000 and 7000
select amount,date
from combined_expenses
where amount between 3000 and 7000;

-- 13. Get the amount with dates starts with 6
select amount,date
from combined_expenses
where amount Like '6%';

-- 14. Get categories which are subscription(total number)
select count(categories) as total_categories
from combined_expenses
where categories='subscription';



-- 15.Find everything which was their on 5th november 2024
select * 
from combined_expenses
where date='2024-11-05';

-- 16. List the number of subsciption from order of highest
select date,categories,amount,cashback
from combined_expenses
where categories='subscription'
order by amount desc
limit 10;


-- 17. write total cashback received in the month of july with payment_mode of debit_card
select payment_mode,sum(cashback) as Cashback_received,extract(month from date) as month
from combined_expenses
where date between '2024-07-01' and '2024-07-31' and payment_mode='debit_card'
group by month;

-- 18. Updating the amount of all date of 2024-01-06
SET SQL_SAFE_UPDATES = 0;
update combined_expenses
set amount='5000'
where date='2024-01-06';

select * from combined_expenses
where amount=5000;

-- 19. Deleting row of date 2024-09-3 where payment_mode is cash
delete from combined_expenses
where date='2024-09-03' and payment_mode='cash';


-- 20. count  amount between 4000 and 5000 with cashback more than average
select count(amount) as total_amount, avg(cashback) 
from combined_expenses
where amount between '4000' and '5000' and cashback >(select avg(cashback) from combined_expenses);


select * from combined_expenses;
