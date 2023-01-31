from multiprocessing import context
from django.shortcuts import render, get_object_or_404,redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required




def store(request):
    
 
    return render(request, 'home.html')

def dashboard(request):
    return render(request, "dashboard.html")

# def product_detail(request, id):
#     if request.user.is_authenticated:
#         product = get_object_or_404(Product, pk=id)
#         context = {'product': product}
#         return render(request, 'store/product_detail.html', context)
#     else:
#         return redirect('/accounts/login')

# @login_required(login_url='accounts/login')    
# def checkout(request):
#     rawcart = Cart.objects.filter(user=request.user)
#     for item in rawcart:
#         if item.product_qty > item.product.quantity :
#             Cart.objects.delete(id = item.id)
#     cartitems = Cart.objects.filter(user=request.user)
#     total_price = 0
#     for item in cartitems:
#         total_price = total_price + item.product.price * item.product_qty
#     userprofile = Profile.objects.filter(user = request.user).first()
#     contacts=Contact.objects.all()     
#     context = {'cartitems':cartitems, 'total_price':total_price, 'userprofile':userprofile,'contacts':contacts}
#     return render(request, 'store/checkout.html', context)

# @login_required(login_url='accounts/login')    
# def addtocart(request):
#     if request.method =='POST':
#         if request.user.is_authenticated:
#             prod_id = int(request.POST.get('product_id'))
#             product_check = Product.objects.get(id=prod_id)
#             if(product_check):
#                 if(Cart.objects.filter(user = request.user.id,product_id = prod_id)):
#                     return JsonResponse({'status': 'Product exist in cart'})
#                 else:
#                     prod_qty = int(request.POST.get('product_qty'))
#                     if product_check.quantity >= prod_qty:
#                         Cart.objects.create(user=request.user, product_id=prod_id, product_qty = prod_qty)
#                         return JsonResponse({'status': 'Product added successfully'})  
#                     else:
#                         return JsonResponse({'status':"Only "+ str(product_check.quantity) +" available " })    
#             else: 
#                 return JsonResponse({'status': 'No such product'})      
#         else:
#              return JsonResponse({'status': 'Login to continue'})    
#     return redirect('/')


# @login_required(login_url='accounts/login')    
# def cart(request):
#     cart = Cart.objects.filter(user = request.user)
#     contacts=Contact.objects.all() 
#     context = {'cart':cart,'contacts':contacts} 
#     return render(request, 'store/cart.html', context)


# @login_required(login_url='accounts/login') 
# def updatecart(request):
#     if request.method =='POST':
#         prod_id = int(request.POST.get('product_id'))
#         if(Cart.objects.filter(user = request.user, product_id=prod_id)):
#             prod_qty = int(request.POST.get('product_qty'))
#             cart = Cart.objects.get( product_id=prod_id, user=request.user)
#             cart.product_qty= prod_qty
#             cart.save()
#             return JsonResponse({'status': "Product updated successfully"})                   
#     return redirect('/')


# @login_required(login_url='accounts/login')     
# def deletecartitem(request):
#     if request.method =='POST':
#         prod_id = int(request.POST.get('product_id'))
#         if(Cart.objects.filter(user = request.user, product_id=prod_id)):
#             cartitem = Cart.objects.get(product_id=prod_id, user=request.user)
#             cartitem.delete()
#             return JsonResponse({'status': "Product deleted successfully"})            
                   
#     return redirect('cart')
    
# @login_required(login_url='accounts/login')    
# def placeorder(request):
#     if request.method =='POST':
#         currentuser = User.objects.filter(id=request.user.id).first()
#         if not currentuser.first_name:
#             currentuser.first_name =request.POST.get('first_name')
#             currentuser.last_name =request.POST.get('last_name')
#             currentuser.save()
#         if not Profile.objects.filter(user=request.user):
#             userprofile = Profile()
#             userprofile.user = request.user
#             userprofile.phone = request.POST.get('phone')
#             userprofile.address1 = request.POST.get('address1')
#             userprofile.address2 = request.POST.get('address2')
#             userprofile.country = request.POST.get('country')
#             userprofile.city = request.POST.get('city')
#             userprofile.state = request.POST.get('state')
#             userprofile.zipcode = request.POST.get('zipcode')
#             userprofile.save()
            
#         neworder = Order()
#         neworder.user = request.user
#         neworder.first_name = request.POST.get('first_name')
#         neworder.last_name = request.POST.get('last_name')
#         neworder.email = request.POST.get('email')
#         neworder.phone = request.POST.get('phone')
#         neworder.address1 = request.POST.get('address1')
#         neworder.address2 = request.POST.get('address2')
#         neworder.country = request.POST.get('country')
#         neworder.city = request.POST.get('city')
#         neworder.state = request.POST.get('state')
#         neworder.zipcode = request.POST.get('zipcode')
#         neworder.payment_mode = request.POST.get('payment_mode')
#         cart = Cart.objects.filter(user = request.user)
#         cart_total_price = 0
#         for item in cart:
#             cart_total_price = cart_total_price + item.product.price * item.product_qty
#         neworder.total_price = cart_total_price    
#         trackno = str(random.randint(11111111,99999999))
#         while Order.objects.filter(tracking_number = trackno) is None:
#             trackno = str(random.randint(11111111,99999999))
#         neworder.tracking_number = trackno
#         neworder.save()
#         neworderitems = Cart.objects.filter(user = request.user)
#         for item in neworderitems:
#             OrderItem.objects.create(
#                 order = neworder,
#                 product = item.product,
#                 price = item.product.price,
#                 quantity = item.product_qty
#                 ) 
#             #decrease item fro stock
#             orderproduct =Product.objects.filter(id=item.product_id).first()
#             orderproduct.quantity=orderproduct.quantity -item.product_qty
#             orderproduct.save()
#             #To clear user's cart
#         Cart.objects.filter(user=request.user).delete()
#         ##Payment mode
#         payMode = request.POST.get('payment_mode')
#         if(payMode == "Pay by PayPal"):
#             return JsonResponse({'status':"Your order has been placed successfully"})
#         else:                
#             messages.success(request,"Your order has been placed successfully")                            
                
#         return redirect('/')
    

# @login_required(login_url='accounts/login')     
# def myorders(request):
#     orders = Order.objects.filter(user=request.user)
#     contacts=Contact.objects.all() 
#     context ={'orders':orders, 'contacts':contacts}
#     return render(request,'store/orders.html',context)    


# @login_required(login_url='accounts/login')     
# def vieworder(request,t_no):
    
#     order = Order.objects.filter(tracking_number=t_no).filter(user=request.user).first()
#     orderitems = OrderItem.objects.filter(order=order)
#     contacts=Contact.objects.all() 
#     context ={'order':order,'orderitems':orderitems,'contacts':contacts}
#     return render(request,'store/view-order.html',context)  


# @login_required
# def search(request):
#     if request.method == 'POST':
#         search = request.POST['search']
#         products = Product.objects.filter(name__contains=search)
#         contacts=Contact.objects.all() 
#         #context = { 'search':search,'products':products}
#         return render(request, 'store/search.html',{'search':search,'products':products,'contacts':contacts})
#     else:       
#         return render(request, 'store/search.html', context)

# from django.views import View

# class TaskDeleteView(View):    
#     def get(self,request, pk, *args, **kwargs):
#         if request=='POST':
#             task = Cart.objects.get(pk=pk)
#             task.delete()
#             messages.success(request, f' Delete success')
#         return redirect("cart")