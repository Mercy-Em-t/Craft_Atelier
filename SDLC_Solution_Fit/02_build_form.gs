/**
 * Google Apps Script to auto-generate the Solution-Fit Survey Form
 * Run this function in script.google.com to deploy the form.
 */
function createSolutionFitForm() {
  var form = FormApp.create('Craft Atelier - Solution Fit Interview Form');
  form.setDescription('Thank you for participating in our UX prototype review. Please refer to the printed UI sketches provided during the interview.');
  
  form.addMultipleChoiceItem()
      .setTitle('Are you Left-Handed or Right-Handed?')
      .setChoiceValues(['Right-Handed', 'Left-Handed', 'Ambidextrous'])
      .setRequired(true);
      
  form.addParagraphTextItem()
      .setTitle('Tell me about the last time you tried to learn a new physical craft. What was the hardest part?')
      .setRequired(true);
      
  form.addParagraphTextItem()
      .setTitle('Looking at the "Interactive Tutorial" screen mockup, what would you click if you got stuck?')
      .setRequired(true);
      
  form.addParagraphTextItem()
      .setTitle('What are your immediate assumptions about the "SOS" button?')
      .setRequired(true);
      
  form.addScaleItem()
      .setTitle('How likely are you to use a live video call feature for crafting help?')
      .setBounds(1, 5)
      .setRequired(true);
      
  Logger.log('Form generated successfully. URL to share: ' + form.getPublishedUrl());
  Logger.log('Edit URL: ' + form.getEditUrl());
}
