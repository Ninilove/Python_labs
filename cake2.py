# Write a program that will ask for a user body weight in pound and convert it in kilogram

weight_in_lbs = float(input('Whats your body weight in lbs?:\t'))

# Convert pounds to kilograms

weight_in_kg = weight_in_lbs * 0.433992

# Print the result rounded to 3 decimal places using the format specifier f"{value:nf} to round the result to 3 decimal places

print(f'Your body weight is {weight_in_lbs} in pound, and the equivalent is {weight_in_kg:.3f} in kg. Thank you')