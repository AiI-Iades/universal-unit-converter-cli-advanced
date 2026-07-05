def convert_unit(unit_from, unit_to, value):
    # Multi-category conversion logic
    if unit_from in ['CO2_tons', 'PM2_5_mu_g_m3'] and unit_to in ['CO2_kg', 'PM_5_ppm']:
        return environmental_conversion(unit_from, unit_to, value)
    elif unit_from in ['GPA', 'Credit_hours'] and unit_to in ['Percentage', 'Grade_point']:
        return education_conversion(unit_from, unit_to, value)
    elif unit_from in ['mg', 'mcg'] and unit_to in ['grams', 'kg']:
        return medical_conversion(unit_from, unit_to, value)
    else:
        return standard_conversion(unit_from, unit_to, value)

if __name__ == '__main__':
    print(convert_unit(input('From unit: ').lower(), input('To unit: ').lower(), float(input('Value: '))))