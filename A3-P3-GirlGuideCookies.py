#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #:     W0443556
#Student Name:  Kyle Preston



def guides_information(girlguideinput):
    totalboxes_sold = 0 # <<<<<I was having issues with this function and I used ChatGPT to fix  structure errors, I was putting it after boxes sold(Line 10 reference) but the issue was it wasn't holding the values for loop list.>>>>
    guides_data = []


    for girlguides in range(1, girlguideinput + 1 ):   #depending on what the girlguideinput is, the beginning value will always start 1(0) to girlguidevalue + 1 so it bypasses the 0
        guides_name = input(f"Enter the name of guide #{girlguides}: ")   #loop for name^ with # list relating to first input
        boxes_sold = int(input(f"Enter the number of boxes sold by {guides_name}: ")) #loop for boxes sold ^
        
        guides_data.append([guides_name, boxes_sold])  # Store the name and boxes sold in guides_data
        totalboxes_sold += boxes_sold #adding all the inputs into the loop list
        print('\n') 
    
   
    averageboxes_sold = totalboxes_sold / girlguideinput #finding the average from sum of boxes_sold  list  divided by amount of girlguides 
    print(f'The average number of boxes sold by each guide was {averageboxes_sold:.1f}')

    return guides_data, averageboxes_sold,

def prizes(guides_data, averageboxes_sold):
    #Highest selling guide gets a Trip to Girl Guide Jamboree in Aruba!
    #Guides selling more than average gets Super Seller Badge
    #Any guide selling atleast one box  Left over cookies
    #no sales  is blank
    highest_selling = max(guides_data, key=lambda x: x[1])  # Find the guide with the most boxes sold
    
    print(f'\nGuide                 Prizes Won:')
    print('--------------------------------------------------------------------------------------------')
    
    for guides_name, boxes_sold in guides_data:
        prize = ""
        
        if boxes_sold == 0:   # No sales no prize
            prize = "- "
        elif boxes_sold == highest_selling[1]:  # Highest seller
            prize = "Trip to Girl Guide Jamboree in Aruba!"
        elif boxes_sold > averageboxes_sold:  #sold above all guides average
            prize = "Super Seller Badge"
        elif boxes_sold >= 1 and boxes_sold < averageboxes_sold:  # sold atleast 1 box, but below guides average
            prize = "Left over cookies"
        
        print(f"{guides_name:<20} {prize}")  #formatted so any first name up to twenty characters will stay left aligned with any extra spot being filled by blanks followed by printing the prizes







def main():
    #starting input to see how many girl guides are selling cookies
    girlguideinput = int(input(f"Enter the number of guides selling cookies: ")) 
    print('\n')

    # Call the function to get the guides data and average boxes sold
    guides_data, averageboxes_sold = guides_information(girlguideinput) 


    # Call the function to assign and print prizes based on sales data
    prizes(guides_data,averageboxes_sold) 

   
main()
