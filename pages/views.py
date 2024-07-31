# pages/views.py
from django.shortcuts import render, HttpResponse, redirect
from .models import AdminPanel, Stylist, Appointment, Contact
from django.contrib import messages
import json
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
import datetime
from django.core.mail import send_mail
import smtplib
import ssl
from email.message import EmailMessage


def index(request):
    # admin = AdminPanel()
    # admin.code = "famu"
    # return render(request, "index.html", {'admin': admin})
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    return render(request, "contact.html")


def sendemail(request):

    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    subject = "Reply from Pearl Beauty"
    # send_mail(subject, message, email, ["farahhussain611@gmail.com"])
    try:
        if name == "" or email == "" or message == "":
            messages.error(request, "Please fill the form first.")
            return redirect('contact')
        else:
            em = EmailMessage()
            em['To'] = email
            em['From'] = "farahhussain611@gmail.com"
            em['Subject'] = subject
            em.set_content(
                "We have received your message. Thank you for contacting us! We'll get back to you shortly.")

            context = ssl.create_default_context()


            with smtplib.SMTP('smtp.elasticemail.com', 2525) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login('syedmuhammad1111@gmail.com',
                        'D89EE1B10E4414818A6D3A55F4B1CB9CEF40')
                server.sendmail("farahhussain611@gmail.com", email, em.as_string())



        # create a new contact
            contact_obj = Contact.objects.create(
                name=name, email=email, message=message, date=datetime.datetime.now())
            contact_obj.save()

            messages.success(request, "Email sent successfully")

            return redirect('contact')
    except Exception as e:
        messages.error(request, "Something went wrong")
        return redirect('contact')


def appointment(request):
    # admin appointment history page
    appointments = list(Appointment.objects.all())
    appointments.reverse()
    context = {"appointments": appointments}
    print(appointments)
    return render(request, "appointment.html", context)

def admincontact(request):
     # admin contacts history page
    contacts = list(Contact.objects.all())
    contacts.reverse()
    context = {"contacts": contacts}
    return render(request, "admincontact.html", context)


def adminToAddStylist(request):
    if request.method == "POST":
            name = request.POST.get('stylistname')
            price = request.POST.get('stylistprice')
            try:
                if name == "" or price == "":
                    messages.error(
                        request, "Please enter the valid inputs for the given fields.")
                else:
                    try:
                        price = float(price)
                        try:
                            # create stylist table
                            # problem in the 3rd parameter
                            bookeddates = []
                            stylist = Stylist.objects.create(
                                name=name, price=price, bookeddates=json.dumps(bookeddates))
                            stylist.save()
                            messages.info(request, "Stylist added!")
                            return redirect("adminToAddStylist")

                        except Exception as err:
                            messages.error(request, "oops, something went wrong!")

                    except Exception as err:
                        messages.error(request, "Please enter a valid price value.")

            except:
                print("An exception occurred")

    return render(request, "addstylist.html")



def delete(request, id):
    appointment = Appointment.objects.get(id=int(id))
    appointment.delete()
    return redirect("appointment")


def getAdvanceDates(numberofdays):
    date_start = datetime.date.today()
    dates = []

    for day in range(numberofdays):
        date = (date_start + datetime.timedelta(days=day)).strftime("%b %d %Y")
        dates.append(date)
    # printing result
    print("Next K dates list: " + str(dates))
    return dates


# after booked appointment is clicked
def getAppointment(request):
    name = request.POST.get('name')
    contact = request.POST.get('contact')
    package = request.POST.get('package')
    getstylistId = request.POST.get('stylistname')
    selecteddate = request.POST.get('selecteddate')
    description = request.POST.get('description')
    try:
        if name == "" or contact == "" or package == "":
            messages.error(request, "Please fill the form first.")
            return None
        else:
            try:
                contact = int(contact)
            except:
                messages.error(request, "Please enter a valid contact number.")
                return None
                

            # stylist object
            # updating stylist object
            stylist = Stylist.objects.get(id=int(getstylistId))
            stylist_name = stylist.name
            stylist_price = stylist.price
            stylist_price = stylist.price
            stylists_booked_dates = list(eval(stylist.bookeddates))
            stylists_booked_dates.append(selecteddate)
            stylist.bookeddates = str(stylists_booked_dates)
            stylist.save()

            # booking date
            todaydate = str(datetime.datetime.now()).split()[0].split('-')
            todaydate = "/".join(todaydate[-1::-1])
        
            # booking appointment object creation
            appointment = Appointment.objects.create(name=name, contact=contact, package=package, stylistname=stylist_name,
                                                     appointmentdate=selecteddate, bookingdate=todaydate, totalamount=stylist_price, description=description)
            appointment.save()
            selecteddate = selecteddate.split()
            selecteddate = "/".join([selecteddate[1],
                                    selecteddate[0], selecteddate[2]])

            context = {"name": name, "bookingdate": todaydate, "package": package,
                       "stylistname": stylist_name, "appointmentdate": selecteddate, "price": stylist_price}

            return context

    except:
        messages.error(request, "Oops something went wrong.")
        return None


def bookappointment(request):
    stylists = Stylist.objects.all()
    stylists_booked_dates = list(eval(answer.bookeddates)
                                 for answer in stylists)
    stylists_ids = list(answer.id for answer in stylists)
    final_stylists = {}
    advance_3_months_dates = getAdvanceDates(
        40)  # 40 days = 1 month and 10 days
    for i in range(len(stylists_ids)):
        if stylists_booked_dates[i] != []:
            booked_dates_list = set(stylists_booked_dates[i])
            advance_3_months_dates = set(advance_3_months_dates)
            availabe_dates = advance_3_months_dates.difference(
                booked_dates_list)
            final_stylists[str(stylists_ids[i])] = list(availabe_dates)
        else:
            final_stylists[str(stylists_ids[i])] = list(advance_3_months_dates)

    context = {"stylists": stylists, "final_stylists": final_stylists}

    return render(request, "bookappointment.html", context)


# button click pages
def voucher(request):
    try:

        # put in the database and get context to show in voucher
        context = getAppointment(request)
        if context is not None:
            return render(request, "voucher.html", context)
        else:
            return redirect("bookappointment")


    except:
        pass

    return render(request, "voucher.html", context)


def addstylist(request):
    password = request.POST.get('password')
    if password != "famu":
        messages.error(
            request, "Code is not validated. We can't log you in :(")
        return redirect("index")
    else:
        messages.success(request, "successful login! Welcome Admin")
        return render(request, "addstylist.html")
