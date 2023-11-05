function HackUTD2023HomeBuyerInfo()

    % Read the CSV file
    csvFilePath = ("HackUTD-2023-HomeBuyerInfo.csv");
    data = readtable(csvFilePath);

    % Extract relevant columns
    creditScore = data.CreditScore;
    loanAmount = data.LoanAmount;
    appraisalValue = data.AppraisedValue;
    monthlyDebt = data.CarPayment + data.CreditCardPayment + data.MonthlyMortgagePayment;
    grossIncome = data.GrossMonthlyIncome;

    % Calculate LTV ratio
    ltvRatio = loanAmount ./ appraisalValue;

    % Determine if potential homebuyers meet the criteria
    qualifiedHomebuyers = (creditScore >= 640) & (ltvRatio <= 0.95) & (monthlyDebt./grossIncome <= 0.43);
    
    % Calculate the number of people who are not qualified
    notQualifiedHomebuyers = ~qualifiedHomebuyers;

    % Create a bar graph to show the results
    figure;
    bar([sum(qualifiedHomebuyers), sum(notQualifiedHomebuyers)]);
    xlabel('Qualify for Home Purchase');
    ylabel('Number of Potential Buyers');
    title('Potential Homebuyers Qualification');
    xticklabels({'Qualified', 'Not Qualified'});

    % Display the counts above the bars
    text(1, sum(qualifiedHomebuyers), num2str(sum(qualifiedHomebuyers)), 'HorizontalAlignment', 'center', 'VerticalAlignment', 'bottom');
    text(2, sum(notQualifiedHomebuyers), num2str(sum(notQualifiedHomebuyers)), 'HorizontalAlignment', 'center', 'VerticalAlignment', 'bottom');

    % Adjust the plot
    ylim([0 max([sum(qualifiedHomebuyers), sum(notQualifiedHomebuyers)]) + 10]);
    grid on;
end

