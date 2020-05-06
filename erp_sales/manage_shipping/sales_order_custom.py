def calculate_total_weight(doc,method):
    from frappe.util import flt
    total_net_weight = 0.0
    for x in doc.items:
        x.weight = flt(x.weight_per_unit) * flt(x.qty)
        total_net_weight = x.weight
    doc.total_net_weight = total_net_weight