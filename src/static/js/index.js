const sendReportEmail() = () => {
        window.location.href = `/report/dashboard`
        }

const searchProducts() = () => {
        const searchInputValue = document.getElementById("product_search").value;
        window.location.href = `/pages/search/${searchInputValue}`;
    }