import React, { useState } from "react";
import "../Styles/RegistrationForm.css";

const RegistrationForm = () => {
  const [formData, setFormData] = useState({
    Firstname: "",
    Lastname: "",
    Email: "",
    Phone: "",
    College: "",
    YearOfPassing: "",
    Gender: "Female",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleGenderChange = (e) => {
    setFormData((prevData) => ({
      ...prevData,
      Gender: e.target.value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData); // For API call
  };

  return (
    <div className="registration-container">
      <div className="event-banner">
        <img
          src="../src/assets/Banner1.svg"
          alt="Event Banner"
          className="event-banner-image"
        />
      </div>
      <form className="registration-form" onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Firstname"
          className="form-input"
          name="Firstname"
          value={formData.Firstname}
          onChange={handleChange}
        />
        <input
          type="text"
          placeholder="Lastname"
          className="form-input"
          name="Lastname"
          value={formData.Lastname}
          onChange={handleChange}
        />
        <input
          type="email"
          placeholder="Email ID"
          className="form-input"
          name="Email"
          value={formData.Email}
          onChange={handleChange}
        />
        <input
          type="text"
          placeholder="Phone Number"
          className="form-input"
          name="Phone"
          value={formData.Phone}
          onChange={handleChange}
        />
        <input
          type="text"
          placeholder="College Name"
          className="form-input"
          name="College"
          value={formData.College}
          onChange={handleChange}
        />
        <input
          type="number"
          placeholder="Year Of Passing"
          className="form-input"
          name="YearOfPassing"
          value={formData.YearOfPassing}
          onChange={handleChange}
        />
        <div className="gender-container">
          <div className="gender-toggle">
            <input
              type="radio"
              id="male"
              name="Gender"
              value="Male"
              checked={formData.Gender === "Male"}
              onChange={handleGenderChange}
            />
            <label htmlFor="male">Male</label>

            <input
              type="radio"
              id="female"
              name="Gender"
              value="Female"
              checked={formData.Gender === "Female"}
              onChange={handleGenderChange}
            />
            <label htmlFor="female">Female</label>

            <div id="gender-flap">
              <span className="gender-content">{formData.Gender}</span>
            </div>
          </div>
        </div>
        <button type="submit" className="register-button">
          Register
        </button>
      </form>
    </div>
  );
};

export default RegistrationForm;
