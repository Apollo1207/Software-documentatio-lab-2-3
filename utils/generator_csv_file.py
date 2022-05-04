from string import Template

section_templates = {'User': Template('phonenumber$i,firstname$i,lastname$i,email$i,password$i,dateofbirth$i,'
                                      'address$i\n'),
                     'PaymentMethod': Template('paymentsystem$i,cardnumber$i,expiredate$i,cvv $i,country$i\n')}


def generate_csv_file(filename):
    with open(filename, 'w+') as file:
        for section, template in section_templates.items():
            file.write(section + '\n')
            for i in range(1, 500):
                if section in ('User',):
                    file.write(template.substitute(i=i))
                elif section in ('PaymentMethod',):
                    file.write(template.substitute(i=i, j=i + 1 if i + 1 != 250 else 1))
            file.write('\n')
