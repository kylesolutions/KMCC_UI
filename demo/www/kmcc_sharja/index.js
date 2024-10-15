$(document).ready(function () {
  $('#membership').on('submit', function (event) {
    event.preventDefault();
    const first_name = frappe.utils.xss_sanitise($("#first_name").val().trim());
    const last_name = frappe.utils.xss_sanitise($("#last_name").val().trim());
    const phone = frappe.utils.xss_sanitise($("#phone").val().trim());
    const email = frappe.utils.xss_sanitise($("#email").val().trim());
    const iqama_number = frappe.utils.xss_sanitise($("#iqama_number").val().trim());
    const blood_group = frappe.utils.xss_sanitise($("#blood_group").val().trim());
    const age = frappe.utils.xss_sanitise($("#age").val().trim());

    console.log("Form data:", first_name, last_name, phone, email, iqama_number, age);
    frappe.call({
      method: "demo.www.kmcc_sharja.index.create_register_form",

      args: {
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "email": email,
        "iqama_number": iqama_number,
        "blood_group": blood_group,
        "age": age
      },
      callback: function (r) {
        if (r.message === "success") {
          alert('Membership created successfully!');
        } else {
          alert('Registration Completed.');
        }
      },
      error: function (err) {
        console.log("Complete");
        alert('An error occurred during submission.');
      }
    });
  });
});
