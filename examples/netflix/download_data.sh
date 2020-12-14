if [ -z "$KAGGLE_KEY" ]; then
   echo "KAGGLE KEY IS NOT SET!"
   exit 1
fi 

if [[ -f "netflix-prize-data.zip" ]]; then
  echo "Skipping download"
else
    mkdir ~/.kaggle || true
    echo $KAGGLE_KEY  > ~/.kaggle/kaggle.json
    kaggle datasets download -d netflix-inc/netflix-prize-data
    unzip netflix-prize-data.zip -d ~/ludwig/examples/netflix/data
fi
