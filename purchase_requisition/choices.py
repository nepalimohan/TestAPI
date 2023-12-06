from django.db import models


class VerificationChoices(models.TextChoices):
	PENDING = "not verified", "Not Verified"
	EVALUATION = "under evaluation", "Under Evaluation"
	VERIFIED = "verified", "Verified"
		

class StatusChoices(models.TextChoices):
	DRAFT = "draft", "Draft"
	SUBMITTED = "submitted for approval", "Submitted for Approval"
	APPROVED = "approved", "Approved"
	CANCELLED = "cancelled", "Cancelled"

class MainModule(models.TextChoices):
	MASTER = "master dashboard", "Master Dashboard"
	INVENTORY = "inventory", "Inventory"
	PURCHASE = "purchase", "Purchase"
	SALES = "sales", "Sales"
	ACCOUNTING = "accounting", "Accounting"
	EBILLING = "ebilling", "ebilling"
	CDXE = "CDXE", "CDXE"



class ActiveStatus(models.TextChoices):
	ACTIVE = "active", "Active"
	INACTIVE = "inactive", "Inactive"


class PriorityChoices(models.TextChoices):
	HIGH = "high", "High"
	NORMAL = "normal", "Normal"
	LOW = "low", "Low"


class TaskChoices(models.TextChoices):
	PENDING = "pending", "Pending"
	STARTED = "started", "Started"
	DONE = "done", "Done"


class PaymentMethod(models.TextChoices):
	CASH = "cash", "Cash"
	CHEQUE = "cheque", "Cheque"
	BANK_TRANSFER = "banktransfer", "Bank Transfer"


class DateBasedOn(models.TextChoices):
	DAYS = "days", "Days"
	MONTHS = "months", "Months"

	
class DiscountType(models.TextChoices):
	DISCOUNT_PERCENTAGE = "discountpercent", "Discount Percentage"
	DISCOUNT_AMOUNT = "discountamount", "Discount Amount"


class DepreciationMethod(models.TextChoices):
	CASH = "straight line", "Straight Line"
	CHEQUE = "units of production", "Units of Prodution"
	BANK_TRANSFER = "double declining balance", "Double Declining Balance"


class AccoutTypeChoices(models.TextChoices):
	SAVING = "saving", "Saving"
	CURRENT = "current", "Current"


class ChartAccoutTypeChoices(models.TextChoices):
	ASSET = "asset", "Asset"
	LIABILITIES = "liabilities", "Liabilities"
	EQUITY = "equity", "Equity"
	EXPENSES = "expenses", "Expenses"
	INCOME = "income", "Income"


class AccountTransactionType(models.TextChoices):
	PAYMENT = "payment", "Payment"
	RECEIPT = "receipt", "Receipt"
	JOURNAL = "journal", "Journal"
	PURCHASE = "purchase", "Purchase"
	SALES = "sales", "Sales"


class SupplierCustomerType(models.TextChoices):
	INDIVIDUAL = "individual", "Individual"
	COMPANY = "company", "Company"
	PARTNERSHIP = "partnership", "Partnership"


class GenderChoice(models.TextChoices):
	Male = "male", "Male"
	Female = "female", "Female"


class ValuationMethod(models.TextChoices):
	FIFO = "FIFO", "First In First Out"


class VatChoices(models.TextChoices):
	ZERO = "0", "0% VAT"
	THIRTEEN = "13", "13% VAT"
	NONVAT = "non vatable", "Non Vatable"


class ProductType(models.TextChoices):
	GOODS = "goods", "Goods"
	SERVICE = "service", "Service"
	
class ModuleTypeChoices(models.TextChoices):
	SQUOTATION = "squotation", "Sales Quotation"
	PQUOTATION = "prequisition", "Purchase Requistion"
	SORDER = "sorder", "Sales Order"
	PORDER = "porder", "Purchase Order"
	GRN = "grn", "Goods Received Note"
	EXPENSE = "expense", "Expense"
	PRETURN = "preturn", "Purchase Return"
	SINVOICE = "sinvoice", "Sales Invoice"
	PINVOICE = "pinvoice", "Purchase Invoice"
	
class ModuleAccountChoices(models.TextChoices):
	GRN = "grn", "GRN"
	PURCHASEINVOICE = "purchase invoice", "Purchase Invoice"
	SALESINVOICE = "sales invoice", "Sales Invoice"
	EXPENSE = "expense management", "Expense Management"
 
class CrDrChoices(models.TextChoices):
	CR = "cr", "Cr"
	DR = "dr", "Dr"
 
class ModuleFeatureChoices(models.TextChoices):
	BANK = "bank", "Bank"
 
class VerificationChoices(models.TextChoices):
	PENDING = "not verified", "Not Verified"
	EVALUATION = "under evaluation", "Under Evaluation"
	VERIFIED = "verified", "Verified"
 

class UsedStatusChoices(models.TextChoices):
	NOTUSED = "not used", "Not Used"
	PARTIAL = "partial", "Partial"
	COMPLETE = "complete", "Complete"