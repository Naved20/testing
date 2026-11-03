import "./globals.css";

export const metadata = {
  title: "Chartered Bus | Online Bus Bookings Made Easy | Indore Bhopal",
  description:
    "Chartered Bus is India's premier passenger mobility provider. Book AC Sleeper, Volvo Multi-Axle, and Seater bus tickets online across Indore, Bhopal, Pune, Ahmedabad and beyond.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en-US">
      <body>{children}</body>
    </html>
  );
}
