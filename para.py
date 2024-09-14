
# Define the dynamic paragraph with placeholders and bold tags
def get_dynamic_paragraph(total_emi, first_emi, instalment_amount, tenure, last_instalment, loan_processing_fee, loan_amount, interest_charges):
    tenure_minus_one = tenure - 1  # Calculate tenure - 1 outside of the format string
    paragraph = '''
    The difference in repayment amount calculated from the total of instalments given under the detailed repayment schedule i.e., ₹<b>{total_emi}</b> (₹<b>{first_emi}</b> as Pre Installment + ₹<b>{first_emi}</b> as 
    1st Installment + ₹<b>{instalment_amount}</b> * (<b>{tenure}</b> - 2) instalments (<b>{instalment_amount}</b> * (<b>{tenure}</b> - 2)) + ₹<b>{last_instalment}</b> as last instalment) (excluding ₹ <b>{loan_processing_fee}</b> (Loan 
    Processing Fee (incl. GST) & Insurance charges)) vis-à-vis the amount of ₹<b>{total_amount}</b> (₹<b>{loan_amount}</b> Loan amount + ₹<b>{interest_charges}</b> Total Interest + ₹<b>{loan_processing_fee}</b> (Loan Processing 
    Fee (incl. GST) & Insurance charges)) mentioned under Total amount to be paid by the borrower include Insurance charges.<br/> 
    Due to rounding off the instalment amount of ₹<b>{actual_instalment}</b> 
    to ₹<b>{instalment_amount}</b> from 2nd instalment number to <b>{tenure_minus_one}</b> instalment number, under the detailed repayment schedule.<br/>
    The Company shall be charging Interest on a reducing balance basis, i.e., Interest shall be calculated on the principal amount of Facility remaining/ outstanding with the Borrower(s) during a specified period. As 
    the principal balance of the Facility decreases, the applicable Interest shall also reduce. In the event of delay in payment of principal amount of the Facility, Interest payable will increase based on the number of 
    days of delay.<br/>
    For example, if the loan interest rate is 20% and Every Month Instalment (EMI) payable is INR 2000, with a principal component of INR 1500, and if the due date for payment is 20th January and 
    the borrower makes payment on 27th January, there will be an increase in Interest payable equal to 20% * 7 days * INR 1500 / 365 ("Additional Amount”). Failure to pay the said Additional Amount may lead to 
    classification of the Borrower(s)’ account as Special Mention Account/ Non-Performing Asset.<br/>
    *The above Repayment schedule is subject to change as per the date of payment.
    '''
    return paragraph.format(
        total_emi=total_emi,
        first_emi=first_emi,
        instalment_amount=instalment_amount,
        tenure=tenure,
        last_instalment=last_instalment,
        loan_processing_fee=loan_processing_fee,
        total_amount=loan_amount + interest_charges + loan_processing_fee,
        loan_amount=loan_amount,
        interest_charges=interest_charges,
        actual_instalment=instalment_amount,
        tenure_minus_one=tenure_minus_one  # Pass the calculated value
    )


def left_side_para():
    left_side="""
  <para>
<u><b>Terms & Conditions:</b></u>
<br/>
1. This Loan Card Factsheet represents acceptance of Loan disbursed to the borrower including the terms and conditions and disclosure of charges mentioned in the loan agreement.<br/>
2. This Loan Card Factsheet is part of loan agreement held between borrower and Annapurna finance Pvt Ltd.<br/>
3. This Loan Card Factsheet is the repayment schedule (including the principal and interest thereon) for the loan being disbursed to the above-mentioned borrower. It also serves as a receipt for all the money collected from the borrower on countersign by the Annapurna Staff.<br/>
4. For the borrowers opting for insurance coverage, the insurance premium collected is passed on to the Insurance Company at actual as per IRDA guidelines. Insurance cover is optional and is provided directly by the Insurance Company; Annapurna only facilitates this process.<br/>
5. The grant of loan is not linked to any other product/services offered by the MFI.<br/>
6. A borrower is required to pay only those charges which are explicitly mentioned in the Loan Card Factsheet. Besides this, the borrower should also note the following:<br/>
   (a) There are no pre-payment/foreclosure penal charges.<br/>
   (b) Penal charges, if any, for delayed payment is applicable only on the overdue amount and not on the entire loan amount.<br/>
7. A loan account will be classified as NPAs if the entire arrears of interest and principal are unpaid by the borrower for more than 90 days.<br/>
8. It is clarified that loan accounts classified as NPAs may be upgraded as ‘standard’ assets only if entire arrears of interest and principal are paid by the borrower.<br/>
9. Once the account is classified as NPA, the same will be reported to the Credit Bureaus for updating the credit history of the borrower.<br/>
10. In case any account is flagged as an NPA account, then the borrower will not be eligible to avail credit facility from AFPL & it may create future implication for the borrowers to avail credit facility from other Financial Institutions.<br/>
</para>
"""
    return left_side.format()

def right_side_para(a,b,c):
    right_side="""
    <para>
    11. The borrower can also refer to the example given herewith for better understanding of the guidelines.<br/>
    12. If the due date of a loan account is March 31, 2024, and full dues are not received before the lending institution runs the day-end process for this date, the date of overdue shall be March 31, 2024. If it continues to remain overdue, then this account shall get tagged as SMA-1 upon running day-end process on April 30, 2024, i.e., upon completion of 30 days of being continuously overdue. Accordingly, the date of SMA-1 classification for that account shall be April 30, 2024. Similarly, if the account continues to remain overdue, it shall get tagged as SMA2 upon running day-end process on May 30, 2024, and if continues to remain overdue further, it shall get classified as NPA upon running day-end process on June 29, 2024.<br/>
    13. No security deposit/margin is being collected from the borrower on this loan.<br/>
    14. We are committed to Transparency and fair lending practices prescribed by the RBI. <br/>
    15. The company shall be accountable in case of inappropriate behaviour of its employees or of the outsourced agency (if any) and timely redressal of grievances of the Borrower. <br/>
    16. For any queries, feedback, and grievances you can reach us on: Nodal officer: __<<>>__, Email Id: __<<>>__, Contact No: __<<>>__, Principal Nodal Officer- Mr. Subrat Sabyasachi Roy, Mobile No- 8280336056, Email Id - gro@ampl.net.in, Toll Free No – 18008437200, MFIN Toll Free No – 18001021080 and follow the detailed Grievance Redressal Mechanism provided as a part of this Loan Fact Sheet. <br/>
    17. Borrowers can raise any grievance/complaint by contacting through the branch manager, nodal officer, website, email, complaint box or by calling at our tollfree no. 1800-8437-200. If the issue is not resolved within 14 days from the date of complaint, it will be escalated to GRO/PNO. If the complaint is not resolved within 30 days, the complainant may approach the RBI ombudsman. <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    </para>
    """
    return right_side.format(
        a=a,
        b=b,
        c=c
    )

def down_data(a):
    down_para="""
    <para>
    In witness whereof Borrower(s) and Company have here onto respectively set their hands at ___<< >>___ branch on the date mentioned above. I acknowledge that I have understood the key factsheet and the
terms &<br/>conditions mentioned in the document.
</para>
    """
    return down_para.format(a)