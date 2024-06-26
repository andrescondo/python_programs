import csv


class Contact:

    #constructor (parametros(self, ))
    def __init__(self, name, phone, email ):
        #guion bajo sig. es privada
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:

    def __init__(self):
        self._contacts = []


    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()


    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)


    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break
  

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()



    def _print_contact(self, contact):
        print('---*---*---*---*---*---*---*---*---*---*---*')
        print('Nombre: {}'.format(contact.name))
        print('Telefono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('---*---*---*---*---*---*---*---*---*---*---*')



    def _not_found(self):
        print('*********************')
        print('¡No encontrado!')
        print('*********************')


    def update(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                self._print_contact(contact)

            print('INGRESE NUEVOS DATOS')
            newName = str(input('Ingrese nombre: '))
            newPhone = str(input('Ingrese número teléfonico: '))
            newEmail= str(input('Ingrese email: '))

            self._contacts[idx].name = newName 
            self._contacts[idx].phone = newPhone
            self._contacts[idx].email = newEmail
            self._save()
            break

    def _save(self):
        with open('contacts.csv' , 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow( ('name', 'phone', 'email'))

            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))


def run():

    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            
            contact_book.add(row[0],row[1],row[2])
            


    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contacto
            [s]alir

            '''))

        if command == 'a':

            name = str(input('Escriba el nombre del contacto: '))
            phone = str(input('Escribe el telefono del contacto: '))
            email = str(input('Escribe el email del contacto: '))

            contact_book.add(name, phone, email)

        elif command == 'ac':
            name = str(input('Escriba el nombre del contacto: '))

            contact_book.update(name)


        elif command == 'b':
            name = str(input('Escriba el nombre del contacto: '))

            contact_book.search(name)


        elif command == 'e':
            name = str(input('Escriba el nombre del contacto: '))

            contact_book.delete(name)


        elif command == 'l':
            
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('comando no encontrado')



if __name__ == '__main__':
    print('A G E N D A - D E - C O N T A C T O S ')
    run()
