weight = 41.5

#Ground shipping
if weight <=  2:
  cost_ground = weight * 1.50 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4 + 20
else: 
  cost_ground = weight * 4.75 + 20

print(cost_ground)
ground_premium = 125
print(ground_premium)

weight= 41.5
#dropshipping
if weight <=  2:
  drone_ground = weight * 4.50 
elif weight > 2 and weight <= 6:
  drone_ground = weight * 9
elif weight > 6 and weight <= 10:
  drone_ground = weight * 12
else: 
  drone_ground = weight * 14.25


print(drone_ground)



